from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def _compute_section_subtotals(self):
        """ Compute section-wise subtotals for the report """
        sections = {}
        current_section = None
        for line in self.order_line:
            if line.display_type == 'line_section':
                current_section = line.name
                sections[current_section] = 0
            elif line.display_type is False and current_section:
                sections[current_section] += line.price_subtotal
        return sections
