# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
#  This file is part of CGRtools.
#
#  CGRtools is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from .element import Element, FrozenDict
from .groups import GroupXVIII
from .periods import *


class He(Element, PeriodI, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 2

    @property
    def isotopes_distribution(self):
        return FrozenDict({3: 1e-06, 4: 0.999999})

    @property
    def isotopes_masses(self):
        return FrozenDict({3: 3.016029, 4: 4.002603})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return ()


class Ne(Element, PeriodII, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 10

    @property
    def isotopes_distribution(self):
        return FrozenDict({20: 0.9048, 21: 0.0027, 22: 0.0925})

    @property
    def isotopes_masses(self):
        return FrozenDict({20: 19.99244, 21: 20.993847, 22: 21.991386})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return ()


class Ar(Element, PeriodIII, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 18

    @property
    def isotopes_distribution(self):
        return FrozenDict({36: 0.003365, 38: 0.000632, 40: 0.996003})

    @property
    def isotopes_masses(self):
        return FrozenDict({36: 35.967546, 38: 37.962732, 40: 39.962383})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return ()


class Kr(Element, PeriodIV, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 36

    @property
    def isotopes_distribution(self):
        return FrozenDict({78: 0.0035, 80: 0.0228, 82: 0.1158, 83: 0.1149, 84: 0.57, 86: 0.173})

    @property
    def isotopes_masses(self):
        return FrozenDict({78: 77.920386, 80: 79.916378, 82: 81.913485, 83: 82.914136, 84: 83.911507, 86: 85.91061})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return ()


class Xe(Element, PeriodV, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 54

    @property
    def isotopes_distribution(self):
        return FrozenDict({124: 0.0009, 126: 0.0009, 128: 0.0192, 129: 0.2644, 130: 0.0408, 131: 0.2118, 132: 0.2689,
                           134: 0.1044, 136: 0.0887})

    @property
    def isotopes_masses(self):
        return FrozenDict({124: 123.905896, 126: 125.904269, 128: 127.90353, 129: 128.904779, 130: 129.903508,
                           131: 130.905082, 132: 131.904155, 134: 133.905394, 136: 135.90722})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        # XeF2, XeF4, XeF6, XeO3, XeO4, XeO2F2, XeOF4, XeO3F2, [XeO6]4-
        return ((0, False, 0, ((1, 'F'), (1, 'F'))),
                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, False, 0, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (2, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (2, 'O'), (2, 'O'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (1, 'F'), (1, 'F'))),
                (0, False, 0, ((2, 'O'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, False, 0, ((2, 'O'), (2, 'O'), (2, 'O'), (1, 'F'), (1, 'F'))),
                (0, False, 0, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (2, 'O'), (2, 'O'))))


class Rn(Element, PeriodVI, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 86

    @property
    def isotopes_distribution(self):
        return FrozenDict({222: 1.0})

    @property
    def isotopes_masses(self):
        return FrozenDict({222: 222.017578})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return (0, False, 0, ((1, 'F'), (1, 'F'))), (1, False, 0, ((1, 'F'),))


class Og(Element, PeriodVII, GroupXVIII):
    __slots__ = ()

    @property
    def atomic_number(self):
        return 118

    @property
    def isotopes_distribution(self):
        return FrozenDict({294: 1.0})

    @property
    def isotopes_masses(self):
        return FrozenDict({294: 294.0})

    @property
    def _common_valences(self):
        return 0,

    @property
    def _valences_exceptions(self):
        return ()


__all__ = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Og']
