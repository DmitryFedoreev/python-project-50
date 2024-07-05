import argparse
from parser import parse_yaml


def generate_diff(file_path1, file_path2):
    data1 = parse_yaml(file_path1)
    data2 = parse_yaml(file_path2)

    keys = sorted(data1.keys() | data2.keys())
    diff = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"   {key}: {data1[key]}")
            else:
                diff.append(f" - {key}: {data1[key]}")
                diff.append(f" + {key}: {data2[key]}")
        elif key in data1:
            diff.append(f" - {key}: {data1[key]}")
        else:
            diff.append(f" + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format', type=str, help='set format of output', default='plain'
    )
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
