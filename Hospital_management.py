patients = [

    {"Name": "Alice", "Age": 30, "Disease": "Flu"},

    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},

    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}

]

search_disease = "Flu"

def add_patient_record(name,age,disease):
    patients.append({
        "Name":name,
        "Age":age,
        "Disease":disease
    })

def search_by_disease(disease):

    return f"Patients with {disease}:{list(map(lambda x:x["Name"],filter(lambda x:x["Disease"]==disease,patients)))}"

print(search_by_disease(search_disease))