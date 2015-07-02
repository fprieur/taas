from flask import Flask
import requests
from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET


class ClickExecute(object):

    def __init__(self, **kwargs):
        self.str_type = kwargs.get('str_type', "content")
        self.id = kwargs.get('id', "")
        self.url = kwargs.get('url', "")
        self.expected_url = kwargs.get('expected_url', "")

    def testClick(self, id, url, expected_url):
        process = Popen(["casperjs", "test", "--id="+ id  +"",
                         "--url="+ url + "", "--expected_url="+ expected_url + "",
                         "--xunit=casperjs-files/click_results.xml",
                         "casperjs-files/click.js"],
                        stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        tree = ET.parse('casperjs-files/click_results.xml')
        root = tree.getroot()
        failure_flag = "0"
        result_str = "success"
        for testcase in root:
            failure_flag = testcase.get('failures')
            test_id = testcase.get("test_id")

        if(failure_flag == "1"):
            result_str = "fail"

        results = {
            "state": result_str,
            "test_id": test_id
        }

        return results


