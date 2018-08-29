#!/bin/bash
apcaccess | grep NOMPOWER | sed 's/NOMPOWER ://g' | sed 's/ Watts//g' | sed 's/ //g'
