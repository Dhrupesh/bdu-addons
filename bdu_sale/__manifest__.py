# -*- encoding: utf-8 -*-
##############################################################################
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company like Veritos.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
##############################################################################

{
    'name'       : 'BDU sales',
    'version'    : '0.1',
    'category'   : 'sale',
    'description': """
BDU specific modifications:

a) filters and grouping in sale advertising: complete replacement of standard set\n
b) title grouping added to facilitate filtering per title group\n
The latter based on sales teams to circumvent additional administration\n
Note that by using sales teams only direct sales teams will be used to group products\n
Note that results from title group filtering (by title) differ from salesteam group (by salesperson) 


    """,
    'author'  	 : 'D. Prosee',
    'website' 	 : 'http://www.bdu.nl',
    'depends' 	 : [
    				'sale_advertising_order',
                    #'bdu_crm',
    			   ],
    'data'    	 : [
		            "views/sale_advertising_view_inherited.xml",
                    "views/sale_advertising_issue_form_inherited.xml",
    			   ],
    'demo'    	 : [
    			   ],
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

