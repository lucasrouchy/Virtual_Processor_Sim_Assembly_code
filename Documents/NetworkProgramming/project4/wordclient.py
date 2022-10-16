import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    global packet_buffer
    
    while True:
        packet_buffer_size = len(packet_buffer)
        # if the buffer size is greater than 2 we know that the first 2 bytes will the length of the word encoded as a big endian number. 
        if packet_buffer_size > 2:
            # converts the big endian numbers to ints to get the int representation of the lenght of the word.
            length_bytes = int.from_bytes(packet_buffer[:2], 'big')
            #int length representation of the word from the packet.
            packet_word_length = length_bytes + 2
            # Now that we have the word packet length as an integer we can compare that to the lenght of the buffer size to see if there is a next word.
            if packet_buffer_size >= packet_word_length:
                # word packet variable ends at the lenght of the string + the 2 big endian bytes that represent the lenght.
                word_packet = packet_buffer[:packet_word_length]
                # now that we have the word packet variable we can set the packet_buffer to start at the end of the last word. This gives us a clean packet_buffer without the first word
                packet_buffer = packet_buffer[packet_word_length:]

                return word_packet
        data = s.recv(5)
        if len(data) == 0:
            return None
        packet_buffer = packet_buffer + data

        



    


def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """

    # TODO -- Write me!

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
