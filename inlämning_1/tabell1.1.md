  p AND S <=> p                       identitet
  
  p OR S <=> p
  ----------------------
  p OR S <=> S                        dominans
  
  p AND F <=> F 
  ----------------------
  p OR NOT p <=> S                    tautologi
  
  p AND NOT p <=> F                   motsägelse
  ----------------------
  p OR p <=> p                        idempotens
  
  p AND p <=> p 
  ----------------------
  NOT(NOTp) <=> p                     dubbel negation
  ----------------------
  p OR q <=> q OR p                   kommutavitet
  
  p AND q <=> q AND p 
  ----------------------
  p OR ( q AND r) <=> (p OR q) AND (p OR r) distributivitet
  
  p AND (q OR r) <=> (p AND q) OR (p AND r)
  ------------------------------------------
