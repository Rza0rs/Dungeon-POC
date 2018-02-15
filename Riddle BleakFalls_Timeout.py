from threading import Timer
print('1: Precisely one of these statements is untrue\n',
      '2: Precisely two of these statements are untrue\n',
      '3: Precisely three of these statements are untrue\n',
      '4: Precisely four of these statements are untrue\n',
      '5: Precisely five of these statements are untrue\n',
      '6: Precisely six of these statements are untrue\n',
      '7: Precisely seven of these statements are untrue\n',
      '8: Precisely eight of these statements are untrue\n',
      '9: Precisely nine of these statements are untrue\n',
      '10: Precisely ten of these statements are untrue.\n')
#=================================================================================
#=================================================================================

while True:
    timeout = 20
    t = Timer(timeout, print, ['Times up. Try again'])
    t.start()
    rdl_dung = input('Which statement is true?, Answer with the number assosiated to statement. You have 20 seconds.\n')

    if rdl_dung == '9':
        print('The answer is statement 9, you have answered correctly.')
        break
    elif rdl_dung != '9':
        print ('You have answered incorrectly.Try again')
    else:
        t.cancel()
        break