CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    middle_name TEXT,
    passport_number TEXT,
    birth_date DATE,
    gender TEXT,
    address TEXT,
    phone_number TEXT,
    email TEXT,
    medical_card_number TEXT,
    medical_card_issue_date DATE,
    last_visit_date DATE,
    next_visit_date DATE,
    insurance_policy_number TEXT,
    insurance_policy_expiry_date DATE
);

CREATE TABLE MedicalProcedures (
    procedure_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    procedure_date DATE,
    doctor_name TEXT,
    procedure_type TEXT,
    procedure_name TEXT,
    procedure_results TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

INSERT INTO Patients VALUES
(1, 'Иван', 'Иванов', 'Иванович', '1234 567890', '1980-01-01', 'М', 'ул. Пушкина, д.10', '123-45-67', 'ivanov@example.com', 'MC001', '2020-01-01', '2021-01-01', '2022-01-01', '123456789', '2023-01-01'),
(2, 'Петр', 'Петров', 'Петрович', '0987 654321', '1975-05-05', 'М', 'пр. Ленина, д.20', '987-65-43', 'petrov@example.com', 'MC002', '2019-01-01', '2020-01-01', '2021-01-01', '987654321', '2022-01-01');

INSERT INTO MedicalProcedures VALUES
(1, 1, '2021-06-15', 'Доктор Сидоров', 'лабораторное исследование', 'Анализ крови', 'Нормальные показатели'),
(2, 2, '2021-06-20', 'Доктор Иванова', 'инструментальная диагностика', 'УЗИ органов брюшной полости', 'Обнаружены камни в желчном пузыре');
