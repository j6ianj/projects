#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class Employee {
private:
    string name;
    string role; // Added member variable for employee's role
    double hourlyRate;
    double hours;

public:
    Employee(string name, string role, double hourlyRate, double hours) {
        this->name = name;
        this->role = role;
        this->hourlyRate = hourlyRate;
        this->hours = hours;
    }

    string getName() const {
        return name;
    };

    string getRole() const { // Added getter for role
        return role;
    }

    double getRate() const {
        return hourlyRate;
    };

    double getHours() const {
        return hours;
    };

    double grossPay() const {
        return hourlyRate * hours;
    }
};

int main() {
    vector<Employee> employees;
    
    cout << "\t\t\t\t\t\tPayroll System Menu" << endl;

    while (true) {
        cout << "1. Get payroll info for employee" << endl;
        cout << "2. Exit" << endl;
        cout << "Enter your choice: ";

        int opt;
        cin >> opt;

        if (opt == 1) {
            string name, role; // Added role variable
            double hourlyRate, hours;
            cout << "Enter employee's name: ";
            cin.ignore();
            getline(cin, name);
            cout << "Enter employee's role: ";
            getline(cin, role);
            cout << "Enter hourly rate: ";
            cin >> hourlyRate;
            cout << "Enter hours worked: ";
            cin >> hours;
            employees.push_back(Employee(name, role, hourlyRate, hours));
        } else if (opt == 2) {
            // Save data to file before exiting
            ofstream outFile("employee_data.txt");
            if (outFile.is_open()) {
                for (const auto& emp : employees) {
                    outFile << "Name: " << emp.getName() << ", Role: " << emp.getRole() << ", Hourly Rate: " << emp.getRate() << ", Hours Worked: " << emp.getHours() << ", Gross Pay: " << emp.grossPay() << endl;
                }
                outFile.close();
            } else {
                cout << "Unable to open file for writing!" << endl;
            }
            break;
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
