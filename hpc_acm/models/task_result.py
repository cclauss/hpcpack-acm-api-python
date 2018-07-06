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


class TaskResult(object):
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
        'job_id': 'int',
        'task_id': 'int',
        'node_name': 'str',
        'command_line': 'str',
        'exited': 'bool',
        'exit_code': 'int',
        'result_key': 'str',
        'task_requeue_count': 'int',
        'message': 'str',
        'filtered_result': 'str',
        'number_of_processes': 'int',
        'process_ids': 'str',
        'kernel_processor_time': 'int',
        'user_processor_time': 'int',
        'working_set': 'int',
        'primary_task': 'bool'
    }

    attribute_map = {
        'job_id': 'jobId',
        'task_id': 'taskId',
        'node_name': 'nodeName',
        'command_line': 'commandLine',
        'exited': 'exited',
        'exit_code': 'exitCode',
        'result_key': 'resultKey',
        'task_requeue_count': 'taskRequeueCount',
        'message': 'message',
        'filtered_result': 'filteredResult',
        'number_of_processes': 'numberOfProcesses',
        'process_ids': 'processIds',
        'kernel_processor_time': 'kernelProcessorTime',
        'user_processor_time': 'userProcessorTime',
        'working_set': 'workingSet',
        'primary_task': 'primaryTask'
    }

    def __init__(self, job_id=None, task_id=None, node_name=None, command_line=None, exited=None, exit_code=None, result_key=None, task_requeue_count=None, message=None, filtered_result=None, number_of_processes=None, process_ids=None, kernel_processor_time=None, user_processor_time=None, working_set=None, primary_task=None):  # noqa: E501
        """TaskResult - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._task_id = None
        self._node_name = None
        self._command_line = None
        self._exited = None
        self._exit_code = None
        self._result_key = None
        self._task_requeue_count = None
        self._message = None
        self._filtered_result = None
        self._number_of_processes = None
        self._process_ids = None
        self._kernel_processor_time = None
        self._user_processor_time = None
        self._working_set = None
        self._primary_task = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if task_id is not None:
            self.task_id = task_id
        if node_name is not None:
            self.node_name = node_name
        if command_line is not None:
            self.command_line = command_line
        if exited is not None:
            self.exited = exited
        if exit_code is not None:
            self.exit_code = exit_code
        if result_key is not None:
            self.result_key = result_key
        if task_requeue_count is not None:
            self.task_requeue_count = task_requeue_count
        if message is not None:
            self.message = message
        if filtered_result is not None:
            self.filtered_result = filtered_result
        if number_of_processes is not None:
            self.number_of_processes = number_of_processes
        if process_ids is not None:
            self.process_ids = process_ids
        if kernel_processor_time is not None:
            self.kernel_processor_time = kernel_processor_time
        if user_processor_time is not None:
            self.user_processor_time = user_processor_time
        if working_set is not None:
            self.working_set = working_set
        if primary_task is not None:
            self.primary_task = primary_task

    @property
    def job_id(self):
        """Gets the job_id of this TaskResult.  # noqa: E501


        :return: The job_id of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this TaskResult.


        :param job_id: The job_id of this TaskResult.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def task_id(self):
        """Gets the task_id of this TaskResult.  # noqa: E501


        :return: The task_id of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskResult.


        :param task_id: The task_id of this TaskResult.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def node_name(self):
        """Gets the node_name of this TaskResult.  # noqa: E501

        The name of the node on which the task runs  # noqa: E501

        :return: The node_name of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this TaskResult.

        The name of the node on which the task runs  # noqa: E501

        :param node_name: The node_name of this TaskResult.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def command_line(self):
        """Gets the command_line of this TaskResult.  # noqa: E501

        Available only for ClusRun task  # noqa: E501

        :return: The command_line of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._command_line

    @command_line.setter
    def command_line(self, command_line):
        """Sets the command_line of this TaskResult.

        Available only for ClusRun task  # noqa: E501

        :param command_line: The command_line of this TaskResult.  # noqa: E501
        :type: str
        """

        self._command_line = command_line

    @property
    def exited(self):
        """Gets the exited of this TaskResult.  # noqa: E501


        :return: The exited of this TaskResult.  # noqa: E501
        :rtype: bool
        """
        return self._exited

    @exited.setter
    def exited(self, exited):
        """Sets the exited of this TaskResult.


        :param exited: The exited of this TaskResult.  # noqa: E501
        :type: bool
        """

        self._exited = exited

    @property
    def exit_code(self):
        """Gets the exit_code of this TaskResult.  # noqa: E501


        :return: The exit_code of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this TaskResult.


        :param exit_code: The exit_code of this TaskResult.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def result_key(self):
        """Gets the result_key of this TaskResult.  # noqa: E501


        :return: The result_key of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._result_key

    @result_key.setter
    def result_key(self, result_key):
        """Sets the result_key of this TaskResult.


        :param result_key: The result_key of this TaskResult.  # noqa: E501
        :type: str
        """

        self._result_key = result_key

    @property
    def task_requeue_count(self):
        """Gets the task_requeue_count of this TaskResult.  # noqa: E501

        The number of times the task is requeued  # noqa: E501

        :return: The task_requeue_count of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._task_requeue_count

    @task_requeue_count.setter
    def task_requeue_count(self, task_requeue_count):
        """Sets the task_requeue_count of this TaskResult.

        The number of times the task is requeued  # noqa: E501

        :param task_requeue_count: The task_requeue_count of this TaskResult.  # noqa: E501
        :type: int
        """

        self._task_requeue_count = task_requeue_count

    @property
    def message(self):
        """Gets the message of this TaskResult.  # noqa: E501


        :return: The message of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TaskResult.


        :param message: The message of this TaskResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def filtered_result(self):
        """Gets the filtered_result of this TaskResult.  # noqa: E501


        :return: The filtered_result of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._filtered_result

    @filtered_result.setter
    def filtered_result(self, filtered_result):
        """Sets the filtered_result of this TaskResult.


        :param filtered_result: The filtered_result of this TaskResult.  # noqa: E501
        :type: str
        """

        self._filtered_result = filtered_result

    @property
    def number_of_processes(self):
        """Gets the number_of_processes of this TaskResult.  # noqa: E501


        :return: The number_of_processes of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._number_of_processes

    @number_of_processes.setter
    def number_of_processes(self, number_of_processes):
        """Sets the number_of_processes of this TaskResult.


        :param number_of_processes: The number_of_processes of this TaskResult.  # noqa: E501
        :type: int
        """

        self._number_of_processes = number_of_processes

    @property
    def process_ids(self):
        """Gets the process_ids of this TaskResult.  # noqa: E501


        :return: The process_ids of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._process_ids

    @process_ids.setter
    def process_ids(self, process_ids):
        """Sets the process_ids of this TaskResult.


        :param process_ids: The process_ids of this TaskResult.  # noqa: E501
        :type: str
        """

        self._process_ids = process_ids

    @property
    def kernel_processor_time(self):
        """Gets the kernel_processor_time of this TaskResult.  # noqa: E501


        :return: The kernel_processor_time of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._kernel_processor_time

    @kernel_processor_time.setter
    def kernel_processor_time(self, kernel_processor_time):
        """Sets the kernel_processor_time of this TaskResult.


        :param kernel_processor_time: The kernel_processor_time of this TaskResult.  # noqa: E501
        :type: int
        """

        self._kernel_processor_time = kernel_processor_time

    @property
    def user_processor_time(self):
        """Gets the user_processor_time of this TaskResult.  # noqa: E501


        :return: The user_processor_time of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._user_processor_time

    @user_processor_time.setter
    def user_processor_time(self, user_processor_time):
        """Sets the user_processor_time of this TaskResult.


        :param user_processor_time: The user_processor_time of this TaskResult.  # noqa: E501
        :type: int
        """

        self._user_processor_time = user_processor_time

    @property
    def working_set(self):
        """Gets the working_set of this TaskResult.  # noqa: E501


        :return: The working_set of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._working_set

    @working_set.setter
    def working_set(self, working_set):
        """Sets the working_set of this TaskResult.


        :param working_set: The working_set of this TaskResult.  # noqa: E501
        :type: int
        """

        self._working_set = working_set

    @property
    def primary_task(self):
        """Gets the primary_task of this TaskResult.  # noqa: E501


        :return: The primary_task of this TaskResult.  # noqa: E501
        :rtype: bool
        """
        return self._primary_task

    @primary_task.setter
    def primary_task(self, primary_task):
        """Sets the primary_task of this TaskResult.


        :param primary_task: The primary_task of this TaskResult.  # noqa: E501
        :type: bool
        """

        self._primary_task = primary_task

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
        if not isinstance(other, TaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
