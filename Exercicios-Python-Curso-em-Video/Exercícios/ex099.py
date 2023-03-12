def maior(* valor):
    print('-=' * 30)
    for c in valor:
        print(c, end=' ')
    print(f'Foram informados {len(valor)} valores ao todo.')
    if len(valor) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(valor)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
