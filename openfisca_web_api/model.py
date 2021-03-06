# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import xml.etree

from openfisca_core import decompositionsxml

from . import conv


def get_decomposition_json(xml_file_path, tax_benefit_system):
    decomposition_tree = xml.etree.ElementTree.parse(xml_file_path)
    decomposition_xml_json = conv.check(decompositionsxml.xml_decomposition_to_json)(decomposition_tree.getroot(),
        state = conv.State)
    decomposition_xml_json = conv.check(decompositionsxml.make_validate_node_xml_json(tax_benefit_system))(
        decomposition_xml_json, state = conv.State)
    decomposition_json = decompositionsxml.transform_node_xml_json_to_json(decomposition_xml_json)
    return decomposition_json


def json_to_cached_instance(value, state = None):
    cache = conv.State.tax_benefit_system_instances_by_json
    if value in cache:
        instance = cache[value]
    else:
        instance = conv.State.TaxBenefitSystem.json_to_instance(value)
        cache[value] = instance
    return instance, None
