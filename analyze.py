import argparse

import utils

def parse_args():
    parser = argparse.ArgumentParser(
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data_dir', type=str, default='data/midi',
                        help='data directory containing .mid files to use for' \
                             'training')
    parser.add_argument('--window_size', type=int, default=20,
                        help='Window size for RNN input per step.')
    return parser.parse_args()


def main():
    args = parse_args()
    args.verbose = True

    try:
        midi_files = utils.midi_files_from_data_dir(args.data_dir)
    except OSError as e:
        utils.log('Error: Invalid --data_dir, {} directory does not exist. Exiting.', args.verbose)
        exit(1)

    num_windows = utils.windows_in_dataset(midi_files, args.window_size)
    avg_num_windows = num_windows / len(midi_files)
    print("Number of windows = %d" % num_windows)
    print("Avg number of windows per file = %d" % avg_num_windows)
    
if __name__ == '__main__':
    main()
