selva = 5000
devi = 2000
mukil = 1000
akhil = 1000
sum_ppf = selva+devi+mukil+akhil

print('Sum = {4}'.format(selva, devi, mukil, akhil, sum_ppf))
      
 
selva_nps = 5000
print('NPS = {0}'.format(selva_nps))


selva_mf = 20000
mukil_mf = 8000
akhil_mf = 8000
devi_mf = 8000
sum_mf = selva_mf+mukil_mf+akhil_mf+devi_mf

print('sum_mf = {4}'.format(selva_mf,mukil_mf,akhil_mf,devi_mf,sum_mf))



sum_tpm = sum_ppf+selva_nps+sum_mf
print('Total per month = {3}'.format(sum_ppf,selva_nps,sum_mf,sum_tpm))

mul = sum_tpm*12
print('yearly = {0}'.format(mul))
