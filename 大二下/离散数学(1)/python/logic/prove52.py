import logic.fvm as fvm

E=['((∀y(∀x(¬Q(x,y))))→(∀x(∀y(¬Q(x,y)))))',
'(((∀y(∀x(¬Q(x,y))))→(∀x(∀y(¬Q(x,y)))))→((¬(∀x(∀y(¬Q(x,y)))))→(¬(∀y (∀x(¬Q(x,y)))))))',
'((¬(∀x(∀y(¬Q(x,y)))))→(¬(∀y(∀x(¬Q(x,y))))))',
'((¬(∀y(∀x(¬Q(x,y)))))→(∃y(¬(∀x(¬Q(x,y))))))',
'((¬(∀x(∀y(¬Q(x,y)))))→(∃y(¬(∀x(¬Q(x,y))))))',
'((∃y(¬(∀x(¬Q(x,y)))))→(∃y(∃xQ(x,y))))',
'((¬(∀x(∀y(¬Q(x,y)))))→(∃y(∃xQ(x,y))))',
'((∃x(∃yQ(x,y)))→(¬(∀x(∀y(¬Q(x,y))))))',
'((∃x(∃yQ(x,y)))→(∃y(∃xQ(x,y))))']
fvm.fvm(E)
