

def internet_transpose(input):
    output_matrix = []
    input_matrix = input.splitlines()

    if input_matrix:
        #Prep matrix
        max_row_length, pad_char = max(map(len,input_matrix)), '\xFF'
        input_matrix = list(map(lambda s: s.ljust(max_row_length, pad_char), input_matrix))

        transposed_padded = map( lambda tup: ''.join(list(tup)), zip(*input_matrix) )
        output_matrix = map( lambda r: r.rstrip(pad_char).replace(pad_char,' '), transposed_padded)

    return '\n'.join(output_matrix).rstrip()


def transpose(input):
    """
    Transposes matrices.
    (N.B. the internet gives this crafty one-liner: zip(*matrix) implemented above, also passes
    all use-cases ...)

    This is still more imperative than it ought to be, but it is at least cleaner and
    more elegant than the embarrassingly panicky version I came up with this-afternoon...
    ... and it passes all the unit tests.
    """

    output_matrix = []
    input_matrix = input.splitlines()

    if input_matrix:

        #Pad all input rows
        max_row_length = max(map(len,input_matrix))
        pad_char = '\xFF' #Let's assume this isn't in the input, and won't annoy string handling.
        input_matrix = list(map(lambda s: s.ljust(max_row_length, pad_char), input_matrix))
        #Every row of the input matrix is now padded with pad_char.

        output_matrix_length = max_row_length  #just so we're clear.

        for i in range(output_matrix_length):
            row = ''
            for j in range(len(input_matrix)):
                row += input_matrix[j][i]
            output_matrix.append(row.rstrip(pad_char).replace(pad_char,' '))

        #placeholder for comment below.


    return '\n'.join(output_matrix).rstrip()




    """
    That's how the story ended after I realised my mistake was to just pad with spaces.
    Everything past this point is purely to describe what I did first.

    TransposeTest.test_mixed_line_length demonstrated that padding/rstripping wouldn't work:
        output_matrix = list(map(lambda s: len(s) < s.rstrip(), output_matrix))

    For test_mixed_line_length, the expected value is:

    expected = [
        "TAAA",
        "h   ", #<-- here, this would be truncated to "h"
        "elll",
        " ooi",
        "lnnn",
        "ogge",
        "n e.",
        "glr",
        "ei ",  #<-- here, ditto.
        "snl",
        "tei",
        " .n",
        "l e",
        "i .",
        "n",
        "e",
        "."
    ]

    Here is the naive approach I took to dealing with that. It passes all the unit tests, but
    I doubt it actually respects the rule of flipping an N x M matrix over its principle triangular axis.

    But it's unlikely to do that by chance.

    Can be pasted where the #placeholder comment is, and it expects "pad_char" to be ' '.

    <code>

        def pprint_matrix(m, title):
            print(f'Matrix {title}')
            for r in m:
                print(f'"{r}"') #to capture the padding, if present.


        row_min_lengths = [len(input_matrix)] * len(output_matrix)

        max_length_seen = 1 #Initialize to the minimum possible length
        for i in range(output_matrix_length-1, 0, -1):
            min_length_curr_row = len(output_matrix[i].rstrip())
            max_length_seen = max(max_length_seen, min_length_curr_row)
            row_min_lengths[i] = max_length_seen

        #For the above input this is [4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1]

        #Now we can clean up, knowing whether an rstrip of trailing spaces is appropriate.

        for i in range(output_matrix_length):
            output_matrix[i] = output_matrix[i].rstrip().ljust(row_min_lengths[i])

    </code>
    """
