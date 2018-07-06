# coding: utf-8

"""
    HPC Web API

    Preview  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from hpc_acm.models.diagnotic_test import DiagnoticTest  # noqa: F401,E501
from hpc_acm.models.event import Event  # noqa: F401,E501
from hpc_acm.models.job_state import JobState  # noqa: F401,E501
from hpc_acm.models.job_type import JobType  # noqa: F401,E501


class Job(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'JobType',
        'id': 'int',
        'name': 'str',
        'command_line': 'str',
        'diagnostic_test': 'DiagnoticTest',
        'state': 'JobState',
        'target_nodes': 'list[str]',
        'progress': 'int',
        'events': 'list[Event]',
        'requeue_count': 'int',
        'fail_job_on_task_failure': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'command_line': 'commandLine',
        'diagnostic_test': 'diagnosticTest',
        'state': 'state',
        'target_nodes': 'targetNodes',
        'progress': 'progress',
        'events': 'events',
        'requeue_count': 'requeueCount',
        'fail_job_on_task_failure': 'failJobOnTaskFailure',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, type=None, id=None, name=None, command_line=None, diagnostic_test=None, state=None, target_nodes=None, progress=None, events=None, requeue_count=None, fail_job_on_task_failure=None, created_at=None, updated_at=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._id = None
        self._name = None
        self._command_line = None
        self._diagnostic_test = None
        self._state = None
        self._target_nodes = None
        self._progress = None
        self._events = None
        self._requeue_count = None
        self._fail_job_on_task_failure = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if command_line is not None:
            self.command_line = command_line
        if diagnostic_test is not None:
            self.diagnostic_test = diagnostic_test
        if state is not None:
            self.state = state
        if target_nodes is not None:
            self.target_nodes = target_nodes
        if progress is not None:
            self.progress = progress
        if events is not None:
            self.events = events
        if requeue_count is not None:
            self.requeue_count = requeue_count
        if fail_job_on_task_failure is not None:
            self.fail_job_on_task_failure = fail_job_on_task_failure
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this Job.  # noqa: E501


        :return: The type of this Job.  # noqa: E501
        :rtype: JobType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Job.


        :param type: The type of this Job.  # noqa: E501
        :type: JobType
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        job id  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        job id  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501

        job name give by user  # noqa: E501

        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        job name give by user  # noqa: E501

        :param name: The name of this Job.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def command_line(self):
        """Gets the command_line of this Job.  # noqa: E501

        Available only for ClusRun job  # noqa: E501

        :return: The command_line of this Job.  # noqa: E501
        :rtype: str
        """
        return self._command_line

    @command_line.setter
    def command_line(self, command_line):
        """Sets the command_line of this Job.

        Available only for ClusRun job  # noqa: E501

        :param command_line: The command_line of this Job.  # noqa: E501
        :type: str
        """

        self._command_line = command_line

    @property
    def diagnostic_test(self):
        """Gets the diagnostic_test of this Job.  # noqa: E501

        Available only for Diagnostics job  # noqa: E501

        :return: The diagnostic_test of this Job.  # noqa: E501
        :rtype: DiagnoticTest
        """
        return self._diagnostic_test

    @diagnostic_test.setter
    def diagnostic_test(self, diagnostic_test):
        """Sets the diagnostic_test of this Job.

        Available only for Diagnostics job  # noqa: E501

        :param diagnostic_test: The diagnostic_test of this Job.  # noqa: E501
        :type: DiagnoticTest
        """

        self._diagnostic_test = diagnostic_test

    @property
    def state(self):
        """Gets the state of this Job.  # noqa: E501


        :return: The state of this Job.  # noqa: E501
        :rtype: JobState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Job.


        :param state: The state of this Job.  # noqa: E501
        :type: JobState
        """

        self._state = state

    @property
    def target_nodes(self):
        """Gets the target_nodes of this Job.  # noqa: E501

        Nodes on which the job runs  # noqa: E501

        :return: The target_nodes of this Job.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_nodes

    @target_nodes.setter
    def target_nodes(self, target_nodes):
        """Sets the target_nodes of this Job.

        Nodes on which the job runs  # noqa: E501

        :param target_nodes: The target_nodes of this Job.  # noqa: E501
        :type: list[str]
        """

        self._target_nodes = target_nodes

    @property
    def progress(self):
        """Gets the progress of this Job.  # noqa: E501

        Job progress  # noqa: E501

        :return: The progress of this Job.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Job.

        Job progress  # noqa: E501

        :param progress: The progress of this Job.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def events(self):
        """Gets the events of this Job.  # noqa: E501

        Events happened in the job  # noqa: E501

        :return: The events of this Job.  # noqa: E501
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Job.

        Events happened in the job  # noqa: E501

        :param events: The events of this Job.  # noqa: E501
        :type: list[Event]
        """

        self._events = events

    @property
    def requeue_count(self):
        """Gets the requeue_count of this Job.  # noqa: E501

        The number of times the job is requeued  # noqa: E501

        :return: The requeue_count of this Job.  # noqa: E501
        :rtype: int
        """
        return self._requeue_count

    @requeue_count.setter
    def requeue_count(self, requeue_count):
        """Sets the requeue_count of this Job.

        The number of times the job is requeued  # noqa: E501

        :param requeue_count: The requeue_count of this Job.  # noqa: E501
        :type: int
        """

        self._requeue_count = requeue_count

    @property
    def fail_job_on_task_failure(self):
        """Gets the fail_job_on_task_failure of this Job.  # noqa: E501


        :return: The fail_job_on_task_failure of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._fail_job_on_task_failure

    @fail_job_on_task_failure.setter
    def fail_job_on_task_failure(self, fail_job_on_task_failure):
        """Sets the fail_job_on_task_failure of this Job.


        :param fail_job_on_task_failure: The fail_job_on_task_failure of this Job.  # noqa: E501
        :type: bool
        """

        self._fail_job_on_task_failure = fail_job_on_task_failure

    @property
    def created_at(self):
        """Gets the created_at of this Job.  # noqa: E501


        :return: The created_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Job.


        :param created_at: The created_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Job.  # noqa: E501


        :return: The updated_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Job.


        :param updated_at: The updated_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
