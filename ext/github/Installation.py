# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import absolute_import

import github.Authorization
import github.Event
import github.Gist
import github.GithubObject
import github.Issue
import github.Notification
import github.Organization
import github.PaginatedList
import github.Plan
import github.Repository
import github.UserKey

from . import Consts

INTEGRATION_PREVIEW_HEADERS = {"Accept": Consts.mediaTypeIntegrationPreview}


class Installation(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Installations. The reference can be found here https://developer.github.com/v3/apps/installations/
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value})

    @property
    def id(self):
        return self._id

    def get_repos(self):
        """
        :calls: `GET /installation/repositories <https://developer.github.com/v3/integrations/installations/#list-repositories>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        url_parameters = dict()

        return github.PaginatedList.PaginatedList(
            contentClass=github.Repository.Repository,
            requester=self._requester,
            firstUrl="/installation/repositories",
            firstParams=url_parameters,
            headers=INTEGRATION_PREVIEW_HEADERS,
            list_item="repositories",
        )

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
