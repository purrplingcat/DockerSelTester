#!/usr/bin/python

import sys, unittest
from custom_text_test_runner import CustomTextTestRunner

if len(sys.argv) < 3:
	print "Usage: TestRunnerReport.py <test_dir> <report_dir>"
	exit(1)

test_modules = unittest.defaultTestLoader.discover(start_dir=sys.argv[1], pattern='*_test.py', top_level_dir=None)
return_code = CustomTextTestRunner(
    verbosity=5,
    results_file_path=sys.argv[2] + '/test_report.json',
    result_screenshots_dir=sys.argv[2] + '/screenshots',
    show_previous_results=True).run(test_modules).returnCode()

print ""
print "*** Test report placed in: " + sys.argv[2] + "/test_report.json"
