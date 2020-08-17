import subprocess
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--value', help='value , REQUIRED', required=False)
args, unknown = parser.parse_known_args()
try:
    ping_response = subprocess.Popen(["ping", "-a", args.value], stdout=subprocess.PIPE).stdout.read()
    result = ping_response.decode('utf-8')
    final ={}
    final.update({'Result' : result})
    with open(str(args.value), 'w') as file:
        file.write(str(final))
        file.close()
except Exception as e:
    sys.stderr.write(str(e))
    exit(-1)
