# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Michell Stuttgart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################

import xml.etree.cElementTree as Et

from sigep.base import RequestBaseSIGEP
from sigep.base import ResponseBase
from sigep.campos import CampoCEP
from sigep.campos import CampoString


class RequestConsultaCEP(RequestBaseSIGEP):

    def __init__(self, cep):
        super(RequestConsultaCEP, self).__init__(ResponseBuscaCEP)
        self.cep = CampoCEP('cep', valor=cep, obrigatorio=True)

    def get_xml(self):
        xml = self.header
        xml += '<cli:consultaCEP>'
        xml += self.cep.get_xml()
        xml += '</cli:consultaCEP>'
        xml += self.footer
        return xml


class ResponseBuscaCEP(ResponseBase):

    def __init__(self):
        super(ResponseBuscaCEP, self).__init__()
        self.logradouro = CampoString('logradouro', obrigatorio=True)
        self.bairro = CampoString('bairro', obrigatorio=True)
        self.cidade = CampoString('cidade', obrigatorio=True)
        self.uf = CampoString('uf', obrigatorio=True, tamanho=2)
        self.complemento = CampoString('complemento')
        self.complemento_2 = CampoString('complemento_2')

    def _parse_xml(self, xml):

        end = Et.fromstring(xml).find('.//return')
        self.logradouro.valor = end.findtext('end')
        self.bairro.valor = end.findtext('bairro')
        self.cidade.valor = end.findtext('cidade')
        self.uf.valor = end.findtext('uf')
        self.complemento.valor = end.findtext('complemento')
        self.complemento_2.valor = end.findtext('complemento2')
