# -*- coding: utf-8 -*-
import pandas as pd

def vectorized_bmi_risk(df, bmi):
  """
  Vectorized - fast function to calculate BMI category and Health Risk 
  """
  df["BMI Category"] = "NA"
  df["Health risk"] = "NA"
  df.loc[(bmi >= 40) , ["BMI Category" ,"Health risk"]] = ["Very severely obese", "Very high risk"]
  df.loc[(bmi>=35) & (bmi<=39.9) , ["BMI Category","Health risk"]] = ["Severely obese", "High risk"]
  df.loc[(bmi>=30) & (bmi<=34.9) , ["BMI Category","Health risk"]] = ["Moderately obese", "Medium risk"]
  df.loc[(bmi>=25) & (bmi<=29.9) , ["BMI Category","Health risk"]] = ["Overweight", "Enhanced risk"]
  df.loc[(bmi>=18.5) & (bmi<=24.9) , ["BMI Category","Health risk"]] = ["Normal weight", "Low risk"]
  df.loc[(bmi<=18.4) , ["BMI Category","Health risk"]] = ["Underweight", "Malnutrition risk"]

  return df

def normal_bmi_risk(row):
  """
  Normal function to calculate BMI category and Health Risk 
  """
  bmi = row.BMI
  if bmi <=18.4:
    category, risk = "Underweight", "Malnutrition risk"
  elif  18.5 <= bmi <= 24.9:
    category, risk = "Normal weight", "Low risk"
  elif  25 <= bmi <= 29.9:
    category, risk = "Overweight", "Enhanced risk"
  elif  30 <= bmi <= 34.9:
    category, risk = "Moderately obese", "Medium risk"
  elif  35 <= bmi <= 39.9:
    category, risk = "Severely obese", "High risk"
  elif  bmi >= 40: 
    category, risk = "Very severely obese", "Very high risk"
  else:
    category, risk = "NA", "NA"
  
  row["BMI Category"] = category
  row["Health risk"] = risk

  return row

def main():
  # read the input json file
  # could read in chunks if the file is too big
  df = pd.read_json(r"input_data.json")
  # calculate the bmi using formula - assuming there are no NA"s or 0 data
  df["BMI"] = df["WeightKg"]/(df["HeightCm"]/100)
  # normal bmi risk calculation using apply
  # df = df.apply(normal_bmi_risk, axis=1)
  
  # vectorized - very fast bmi risk calculation
  df = vectorized_bmi_risk(df, df["BMI"].values)
  # Print to console the result
  output_json = df.to_json(orient="records")
  print(output_json)
  # write to json file if needed
  # df.to_json(r"output_data.json", orient="record")

if __name__=="__main__":
  main()
  

