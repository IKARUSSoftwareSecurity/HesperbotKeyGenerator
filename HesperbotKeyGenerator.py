__author__ = 'elias.t'

from argparse import ArgumentParser

def PrintAllKeys(pairs=False):
    '''
    This method prints all possible (exactly 10,000 keys) on to the console
    The user is able to requres Activation and rCode key pairs or the rCodes for easy uninstall code generation

    The keys are brute-forced but, they are all valid because of consistency checks on activation codes.
    '''

    i = 0
    j = 0
    k = 0
    m = 0
    n = 0
    i1 = 0
    attempt_limit = 10

    # Brute force all possible Activation keys and their rCode pairs
    while i < attempt_limit:
        while j < attempt_limit:
            while k < attempt_limit:
                while m < attempt_limit:
                    while n < attempt_limit:
                        while i1 < attempt_limit:
                            calculation = k*(m + i * 10 + (n + j * 10))
                            strCalculation = str(calculation)
                            calculation_last_digit = int(strCalculation[len(strCalculation)-1])
                            if calculation_last_digit == i1:
                                #print("Found match, key can be generated: "
                                #      "i={0}, j={1}, k={2}, m={3}, n={4}, i1={5}".format(i, j, k, m, n, i1))
                                if pairs == True:
                                    print("Activation key: {0}{1}{2}{3}{4}{5}".format(i, j, k, m, n, i1))
                                    print("Response Code: " + str(GenerateResponseCode(i, j, k, m, n, i1)))
                                else:
                                    print("%06d" % GenerateResponseCode(i, j, k, m, n, i1))
                            i1 += 1
                        n += 1
                        i1 = 0
                    m += 1
                    n = 0
                k += 1
                m = 0
            j += 1
            k = 0
        i += 1
        j = 0

def GenerateResponseCode(i, j, k, m, n, i1):
    '''
    Generates an always valid response (rCode) out of the Activation code.
    '''

    magic_seed_number = "7362095814"
    # 4 6 1 3 5 2
    rCode_digit1 = magic_seed_number[m]
    rCode_digit2 = magic_seed_number[i1]
    rCode_digit3 = magic_seed_number[i]
    rCode_digit4 = magic_seed_number[k]
    rCode_digit5 = magic_seed_number[n]
    rCode_digit6 = magic_seed_number[j]

    return int(rCode_digit1 + rCode_digit2 + rCode_digit3 + rCode_digit4 + rCode_digit5 + rCode_digit6)

if __name__ == "__main__":
    '''
    AndroidOS.Trojan.Hesperbot KeyGenerator

    This is a quick hack tool for generating Activation and response (rCodes) for the AndroidOS.Trojan.Hesperbot [1]
    Android Trojan for testing. This code is part of the documentation [2] that discusses the removal and cracking
    of the same Trojan.

    The current version of this key generator works
    with the supposed "beta" version of Hesperbot, that surfaced in the April of 2014 in Austria.

    •	APK Sample
        o	MD5: a10fae2ad515b4b76ad950ea5ef76f72
        o	SHA1: a5fd87e902ac6eeb8b1f885976d3a38ff4d70b52
        o	SHA256: 88b2801f8963e61e71207d57725d520a41750fad11e5f0a21ac34672d9c0d58e

    •	DEX Sample:
        o	MD5: 3d70ebfce0130c08772bf449d82d1235
        o	SHA1: 8fce71267af12db8578c9676c58ecf6c2c3d0424
        o	SHA256: 9f9930e0eced0d3ba610ff381f0c1e60cceb63e8f64969026ef5c466dc8038ab

    [1] For more information on AndroidOS.Trojan.Hesperbot: Analysis Report AndroidOS.Trojan.Hesperbot
        [Released: 15.04.2014]
    [2] Cracking/Removing self-locking Android Malware [Released: TBA]


    '''
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p','--pairs',
                        help='Prints all Activation/rCode pairs for generating activation keys.',
                        action='store_true')
    group.add_argument('-r','--rcodes',
                        help='Prints all rCodes (formated to 6 digits) and ready for uninstall key generation.',
                        action='store_true')

    args = parser.parse_args()

    if args.pairs:
        PrintAllKeys(True)
    elif args.rcodes:
        PrintAllKeys(False)
