import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, default='', help="the key of the storage")
parser.add_argument("--val", type=str, default='', help="the value of the storage")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")

# если нет файла, создать пустой json
if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as f:
        json.dump({}, f)

#  os.remove(storage_path)

with open(storage_path, 'r') as f:
    storage = json.load(f)

if args.val:
    if args.key not in storage.keys():
        storage[args.key] = [args.val]
    else:
        storage[args.key].append(args.val)

    with open(storage_path, 'w') as f:
        json.dump(storage, f)

else:
    values = storage.get(args.key)
    if values:
        print(*values, sep=', ')
