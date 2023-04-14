# python3
# Artūrs Brūvers 221RDB511 DS-14

def read_input(filename):
    try:
        with open(f"./test/(filename)") as f:
            contents = f.readlines()
        except FileNotFoundError:
            raise ValueError("Missing File")
        except:
            raise ValueError("Reading Error")

    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
   
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
  
    return [0]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
