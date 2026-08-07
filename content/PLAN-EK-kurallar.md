# PLAN — EK KURALLAR

Bu dosya `PLAN-soru-dagilimi.md`'ye eklenen istisnaları taşır (o dosya elle değiştirilmez).

## Kalite kuralı 2 istisnası

Cevabı NOT GIVEN olan sorularda `evidence` boş kalır; gerekçe `not_given_justification`
alanına yazılır. `tools/dogrula.py` zaten NOT GIVEN'ı `evidence` zorunluluğundan muaf
tutuyor — bu kural yazısı aracın davranışına uydurulmuş oluyor, tersi değil.
