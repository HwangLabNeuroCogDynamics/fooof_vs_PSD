imMFrt numpy as np
from pymer4.models import Lm, Lmer, Lm2
import pandas as pd

df = pd.read_csv('Data/fooof_data_youngDataset_forKai.csv')

#grouping variable subID_only
#IV: age
#DV: PO_EO_slope  PO_EO_yint  MF_EO_slope  MF_EO_yint

# no random effects
print(Lm('PO_EO_slope ~ age', data=df).fit())
print(Lm('PO_EO_yint ~ age', data=df).fit())
print(Lm('MF_EO_slope ~ age', data=df).fit())
print(Lm('MF_EO_yint ~ age', data=df).fit())

print(Lmer('PO_EO_slope ~ age + (age |subID_only)', data=df).fit())

# random slope
print(Lmer('PO_EO_slope ~ age + (0 + age |subID_only)', data=df).fit())
print(Lmer('PO_EO_yint ~ age + (0 + age |subID_only)', data=df).fit())
print(Lmer('MF_EO_slope ~ age + (0 + age |subID_only)', data=df).fit())
print(Lmer('MF_EO_yint ~ age + (0 + age |subID_only)', data=df).fit())



# random intercept
print(Lmer('PO_EO_slope ~ age + (1  |subID_only)', data=df).fit())
print(Lmer('PO_EO_yint ~ age + (1 |subID_only)', data=df).fit())
print(Lmer('MF_EO_slope ~ age + (1  |subID_only)', data=df).fit())
print(Lmer('MF_EO_yint ~ age + (1 |subID_only)', data=df).fit())



## using RMS package suggested Isaac:
# This time we use the 'group' argument when initializing the model
df['subID_only'] = df['subID_only'].astype('str')
print(Lm2('PO_EO_slope ~ age', data=df, group='subID_only', ).fit())


#R code and results
# library('rms')
# df <- read.table("fooof_data_youngDataset_forKai.csv", header=TRUE, sep=",")
# robcov(ols(PO_EO_slope ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# robcov(ols(PO_EO_yint ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# robcov(ols(MF_EO_slope ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# robcov(ols(MF_EO_yint ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)


# > robcov(ols(PO_EO_slope ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# Linear Regression Model
 
#  ols(formula = PO_EO_slope ~ age, data = df, x = TRUE, y = TRUE)
 
#                             Model Likelihood     Discrimination    
#                                Ratio Test           Indexes        
#  Obs                 59     LR chi2      1.38    R2       0.023    
#  sigma           0.2344     d.f.            1    R2 adj   0.006    
#  d.f.                57     Pr(> chi2) 0.2397    g        0.041    
#  Cluster ondf$subID_only                                           
#  Clusters            39                                            
 
#  Residuals
 
#       Min       1Q   Median       3Q      Max 
#  -0.53549 -0.15241  0.02861  0.12456  0.68352 
 
 
#            Coef    S.E.   t     Pr(>|t|)
#  Intercept  1.4908 0.1440 10.36 <0.0001 
#  age       -0.0377 0.0296 -1.27 0.2090  
 
# > robcov(ols(PO_EO_yint ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# Linear Regression Model
 
#  ols(formula = PO_EO_yint ~ age, data = df, x = TRUE, y = TRUE)
 
#                             Model Likelihood     Discrimination    
#                                Ratio Test           Indexes        
#  Obs                 59     LR chi2      1.72    R2       0.029    
#  sigma           0.4224     d.f.            1    R2 adj   0.012    
#  d.f.                57     Pr(> chi2) 0.1894    g        0.082    
#  Cluster ondf$subID_only                                           
#  Clusters            39                                            
 
#  Residuals
 
#      Min      1Q  Median      3Q     Max 
#  -1.2565 -0.2291  0.1109  0.2768  0.7415 
 
 
#            Coef     S.E.   t      Pr(>|t|)
#  Intercept -10.1650 0.2584 -39.34 <0.0001 
#  age        -0.0758 0.0576  -1.32 0.1931  
 
# > robcov(ols(MF_EO_slope ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# Linear Regression Model
 
#  ols(formula = MF_EO_slope ~ age, data = df, x = TRUE, y = TRUE)
 
#                             Model Likelihood     Discrimination    
#                                Ratio Test           Indexes        
#  Obs                 59     LR chi2      0.19    R2       0.003    
#  sigma           0.2729     d.f.            1    R2 adj  -0.014    
#  d.f.                57     Pr(> chi2) 0.6615    g        0.018    
#  Cluster ondf$subID_only                                           
#  Clusters            39                                            
 
#  Residuals
 
#       Min       1Q   Median       3Q      Max 
#  -0.74716 -0.17814  0.05834  0.17880  0.62977 
 
 
#            Coef   S.E.   t    Pr(>|t|)
#  Intercept 1.1613 0.2034 5.71 <0.0001 
#  age       0.0162 0.0427 0.38 0.7053  
 
# > robcov(ols(MF_EO_yint ~ age, data = df, x = TRUE, y = TRUE), cluster = df$subID_only)
# Linear Regression Model
 
#  ols(formula = MF_EO_yint ~ age, data = df, x = TRUE, y = TRUE)
 
#                             Model Likelihood     Discrimination    
#                                Ratio Test           Indexes        
#  Obs                 59     LR chi2      0.07    R2       0.001    
#  sigma           0.3727     d.f.            1    R2 adj  -0.016    
#  d.f.                57     Pr(> chi2) 0.7945    g        0.014    
#  Cluster ondf$subID_only                                           
#  Clusters            39                                            
 
#  Residuals
 
#       Min       1Q   Median       3Q      Max 
#  -0.94789 -0.22067  0.03019  0.25331  0.63491 
 
 
#            Coef     S.E.   t      Pr(>|t|)
#  Intercept -10.6540 0.2530 -42.11 <0.0001 
#  age         0.0132 0.0549   0.24 0.8109  