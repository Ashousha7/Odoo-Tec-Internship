from odoo import models, fields, api
from textblob import TextBlob
from transformers import pipeline
import re

# Load the pretrained classifier only once (adjust model as needed)
team_classifier = pipeline("zero-shot-classification",
                           model="facebook/bart-large-mnli")

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    sentiment = fields.Selection([
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative')
    ], string='Sentiment', readonly=True)

    suggested_team_id = fields.Many2one('helpdesk.team', string='Suggested Team', readonly=True)

    @api.model
    def create(self, vals):
        description = vals.get('description', '')
        cleaned_desc = self._strip_html_tags(description)

        sentiment = self._analyze_sentiment(cleaned_desc)
        print(f"\n[SENTIMENT ANALYSIS] ➤ {sentiment}")
        vals['sentiment'] = sentiment

        team = self._suggest_team(cleaned_desc)
        if team:
            print(f"[SUGGESTED TEAM] ➤ {team.name}")
            vals['suggested_team_id'] = team.id

        return super().create(vals)

    def write(self, vals):
        if 'description' in vals:
            cleaned_desc = self._strip_html_tags(vals['description'])

            sentiment = self._analyze_sentiment(cleaned_desc)
            print(f"\n[SENTIMENT ANALYSIS] ➤ {sentiment}")
            vals['sentiment'] = sentiment

            team = self._suggest_team(cleaned_desc)
            if team:
                print(f"[SUGGESTED TEAM] ➤ {team.name}")
                vals['suggested_team_id'] = team.id

        return super().write(vals)

    @staticmethod
    def _strip_html_tags(text):
        return re.sub(r'<.*?>', '', text or '')

    @staticmethod
    def _analyze_sentiment(text):
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            if polarity > 0.1:
                return 'positive'
            elif polarity < -0.1:
                return 'negative'
            else:
                return 'neutral'
        except Exception as e:
            print(f"[ERROR] Sentiment analysis failed: {e}")
            return 'neutral'

    def _suggest_team(self, text):
        try:
            candidate_labels = [
                "Sales Team", "Technical Support", "Financial Team", "Customer Care"
            ]
            result = team_classifier(text, candidate_labels)
            top_label = result['labels'][0]

            return self.env['helpdesk.team'].search([('name', 'ilike', top_label)], limit=1)
        except Exception as e:
            print(f"[ERROR] Team suggestion failed: {e}")
            return None
