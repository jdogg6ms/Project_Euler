#!/usr/bin/env scheme-r5rs
; Project Euler Problem #1
; p1.scm

     
(define (sumfactors n max total) 
  ;(write n )
  (cond ((= n max) total)      
        (else 
            (define running_total (+ total (if (or (= (modulo n 3) 0) (= (modulo n 5) 0))
                n 0)))
            (sumfactors (+ n 1) max running_total)
         )
   )
)
  

