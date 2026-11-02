/*
 * Author:Jaylen Savoie
 * Date: 10-29-2026
 * Description: This version will implement JOPtionPane with ArrayList (dynamic storage). Validation has been added.
 */

package payrollArrayGUI;

import java.util.ArrayList;
import java.util.Scanner;
import java.text.DecimalFormat;
import javax.swing.JOptionPane;

public class PayrollArrayGUI {
	
	//Global Declarations
	static String stringInput = " ";
	//static Employee [] emp = new Employee[100]; //an array of objects
	static ArrayList<Employee> empList = new ArrayList<Employee>();
	static Employee dummy = new Employee(); //Global dummy accessor to Employee class 

	public static void main(String[] args) {
		
		//working variables
		int choice = 0;
		int empCount = 0; // used to keep track of employee currently processed and all employees
		String searchSSN = " ";
		int foundAt = -1; //means not found
		int start = 0;
		
		
		//processes
				start = JOptionPane.showConfirmDialog(null, "Start this program?", "Confirmation", JOptionPane.YES_NO_OPTION);
				if(start == JOptionPane.NO_OPTION) // user does not want to start app
					JOptionPane.showMessageDialog(null, "Thank you for visiting");
				
				else {
					while (choice != 4) {
						choice = menu();
						switch(choice)
						{
						case 1: Employee emp = new Employee();//an instance of an employee
								emp.getSSN();
								emp.getFirst();
								emp.getLast();
								emp.getRate();
								emp.getHours();
								emp.calcGross();
								empList.add(emp);
								empCount++;
								break;
								
						case 2: if (empList.isEmpty())
								JOptionPane.showMessageDialog(null, "Database empty! Add employees first...");
								else {
									
									for(int i = 0; i < empList.size(); ++i)
										empList.get(i).dispReport();
								}
								break;
						case 3: //System.out.println("Enter the SSN to search for: ");
								stringInput = JOptionPane.showInputDialog("Enter the SSN to search for: ");
								searchSSN = stringInput;
								while(!dummy.checkSSN(searchSSN)) { 
									stringInput = JOptionPane.showInputDialog("INVALID SSN! Enter the SSN to search for:  ");
									searchSSN = stringInput;
								}
								foundAt = searchEmployee(searchSSN);
								if (foundAt == -1)
									// System.out.println(searchSSN + " was not found!");
									JOptionPane.showMessageDialog(null, searchSSN + " was not found!");
								else
									empList.get(foundAt).dispReport();
								break;
						case 4: //System.out.println("Goodbye!");
								JOptionPane.showMessageDialog(null, "Thank you for using this app...Goodbye!");
								break;
						default: //System.out.println("Wrong choice...please try again...");
								 JOptionPane.showMessageDialog(null, "Wrong Choice....please try again.");
								
						}//end switch
					}//end while (choice !=4)
			 }//end else	
	}//end public static void main
	
	
	
	public static int menu() {
			int choice = 0;
			String userInput = JOptionPane.showInputDialog(null,"-1-Add employee\n" +
							   "-2-Display all employees\n" +
							   "-3-Search for an employee\n" +
							   "-4-Quit\n" +
								"\tEnter choice 1-4: ");
			while(!dummy.checkMenu(userInput)){
				JOptionPane.showMessageDialog(null, "Inavlid input! Please try again", "Warning", JOptionPane.WARNING_MESSAGE); //Presents warning message if Invalid Input is detected
				userInput = JOptionPane.showInputDialog(null,"-1-Add employee\n" +
						   "-2-Display all employees\n" +
						   "-3-Search for an employee\n" +
						   "-4-Quit\n" +
							"\tEnter choice 1-4: ");
			}
			
			choice = Integer.parseInt(userInput);
			return choice;
		}//end menu()


	public static int searchEmployee(String searchSSN) {
		int i = 0;
		while(i < empList.size()) {
			if (searchSSN.equals(empList.get(i).ssn))
				return i;
			else
				++i;
		}
		return -1;
	}// end searchEmployee
	
} //end class PayrollArray GUI



class Employee
{
	//declarations:
		static DecimalFormat DF = new DecimalFormat("#####0.00");
		
		//object: employee
		String ssn;
		String first;
		String last;
		double rate;
		double hours;
		double gross;
		
		
		//working variables
		Scanner input = new Scanner(System.in);
		String stringInput = " ";
		
		//constructors:
		Employee(){
			ssn = " ";
			first = " ";
			last = " ";
			rate = 0.0;
			hours = 0;
			gross = 0.0;
			
		}//end constructor w/o arguments
		
		Employee(String ssn, String first, String last, double rate, int hours){
			this.ssn = ssn;
			this.first = first;
			this.last = last;
			this.rate = rate;
			this.hours = hours;
		}//end constructor with arguments
		
		void getSSN() {
			//System.out.println("Enter this employee SSN: ");
			stringInput = JOptionPane.showInputDialog("Enter this employee SSN: ");
			while(!checkSSN(stringInput)) {
				stringInput = JOptionPane.showInputDialog("INVALID SSN! Enter this employee SSN: ");
			}
			ssn = stringInput;
		}//end getSSN()
		
		
		void getFirst() {
			//System.out.println("Enter this employee fist name: ");
			stringInput = JOptionPane.showInputDialog("Enter this employee First name (add Middle Name or Hyphenated Name here if neccesary): ");
			while(!checkFirstName(stringInput)) {
				stringInput = JOptionPane.showInputDialog("INVALID FIRST NAME! Enter the employee First Name: ");
			}
			first = stringInput;
		}//end getFirst()
		
		void getLast() {
			//System.out.println("Enter this employee Last Name: ");
			stringInput = JOptionPane.showInputDialog("Enter this employee Last name: ");
			while(!checkLastName(stringInput)) {
				stringInput = JOptionPane.showInputDialog("INVALID LAST NAME! Enter the employee LAST Name: ");
			}
			last = stringInput;
		}//end getLast()
		
		
		void getRate() {
			//System.out.println("Enter this employee rate:$ ");
			stringInput = JOptionPane.showInputDialog("Enter this employee rate:$ ");
			while(!checkRate(stringInput)) {
				stringInput = JOptionPane.showInputDialog("INVALID RATE! Enter the employee rate:$ ");
			}
			rate = Double.parseDouble(stringInput);
		}//end getRate()
		
		
		void getHours() {
			//System.out.println("Enter this employee hours worked: ");
			stringInput = JOptionPane.showInputDialog("Enter this employee hours worked: ");
			while(!checkHours(stringInput)) {
				stringInput = JOptionPane.showInputDialog("INVALID HOURS Enter the employee hours worked: ");
			}
			hours = Double.parseDouble(stringInput);
		}//end getHours()
		
		void calcGross() {
			gross = rate* hours;
		}//end getRate()
		
		void dispReport() {
			
			JOptionPane.showMessageDialog(null, "Emplyee ssn: " + ssn + "\n" +
												"Emplyee First Name:" + first + "\n" +
												"Emplyee Last Name:"  + last + "\n" +	
												"Emplyee Hourly Rate:" + rate + "\n" +
												"Emplyee Hours Worked:" + hours + "\n" +
												"Emplyee Gross Salary:$ " + DF.format(gross) + "\n");
		}// end dispReport
		
		
		
		
//#############################VALIDATION METHODS############################
		
		boolean checkSSN(String input) {
			if(input.length() != 9)
				return false;
			else {
				int i = 0;
				while (i< input.length()) {
					if(!Character.isDigit(input.charAt(i)))
						return false;
					else
						i++;
					
				}//end while
			} // end else
			return true;
		}//end checkSSN
		
		
		
		boolean checkFirstName(String input) {
				int i = 0;
				if (input.length() <= 0) //catches no input from user
					return false;
				else {
					while (i< input.length()) {
						if (!Character.isAlphabetic(input.charAt(i)) && input.charAt(i) != ' ' && input.charAt(i) != '-') 
							/*Detect if there is a number or special character in name allows user to have space for special names (such as Mary-Jane Parker or Mary Jane Parker )
							 * 
							 */
							return false;
						else
							i++;
					 }//end while
				return true;
					}//end else
		}//end checkFirstName
		
		
		boolean checkLastName(String input) {
			int i = 0;
			if (input.length() <= 0) //catches no input from user
				return false;
			else {
				while (i< input.length()) {
					if (!Character.isAlphabetic(input.charAt(i)))
						//Detect if there is a number or special character in  Last Name 
						return false;
					else
						i++;
				 }//end while
			}//end else
		return true;
	}//end checkLastName
		
		boolean checkRate(String input) {
			int i = 0;
			if (input.length() <= 0) //catches no input from user
				return false;
			else {
				while (i< input.length()) {
					if (!Character.isDigit(input.charAt(i)) && input.charAt(i) != '.') //Detect that all characters are digits, allows for '.' to be entered
						return false;
					else
						i++;
				 }//end while
			return true;
		}//end else
	}//end checkRate
	
		
		boolean checkHours(String input) {
			int i = 0;
			if (input.length() <= 0) //catches no input from user
				return false;
			else {
			while (i< input.length()) {
				if (!Character.isDigit(input.charAt(i))  && input.charAt(i) != '.') //Detect that all characters are digits, allows for '.' to be entered
					return false;
				else
					i++;
			 }//end while
		return true;
			}//end else
	}//end checkHours
		
		
		boolean checkMenu(String input) {
			if (input.equals("1") || input.equals("2") || input.equals("3") || input.equals("4")) //checks if input is a valid option
				return true;
			else
				return false;
		}// end checkMenu
		
		
	}//end class


			






