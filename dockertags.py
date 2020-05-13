from argparse import ArgumentParser
import requests

URL = 'https://registry.hub.docker.com/v1/repositories/{image_name}/tags'


def get_arguments():
    arg_parser = ArgumentParser(add_help=True, description='Get docker image tags.')
    arg_parser.add_argument('image', help='Image name')
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()
    response = requests.get(URL.format(image_name=args.image))
    if response:
        for tags in response.json():
            print(tags['name'])
    else:
        print(f'Something gone wrong: {response.status_code}')