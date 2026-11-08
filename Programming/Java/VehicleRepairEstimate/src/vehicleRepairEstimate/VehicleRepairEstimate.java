/*
 * Author: Jaylen Savoie
 * Date: 11/08/2026
 * Description: Vehicle Repair Estimate Manager
 */
package vehicleRepairEstimate;

import javax.swing.JOptionPane;
import java.text.DecimalFormat;
import java.util.ArrayList;

public class VehicleRepairEstimate {
	
	//Global Variables
	static String input = "";
	static RepairJob dummy = new RepairJob();//accessor to RepairJob
	static ArrayList<RepairJob> repairjobList = new ArrayList<RepairJob>(); //Repair Job Array List

	public static void main(String[] args) {
		
		//working variables
		int jobCount = 0;
		String searchJob = " ";
		int foundAt = -1; //means not found
		int start = 0;
		
		start = JOptionPane.showConfirmDialog(null, "Start this program?", "Confirmation", JOptionPane.YES_NO_OPTION);
		if(start == JOptionPane.NO_OPTION) // user does not want to start app
			JOptionPane.showMessageDialog(null, "Thank you for visiting");
		
		else {
		
			
			while (true) {
				int menuSelection = Menu();
				switch (menuSelection) {
				case 1: {
					RepairJob job = new RepairJob();
				
					job.jobID = job.jobID();
					job.country = job.country();
					job.serviceCity = job.serviceCity();
					job.estimatedCost = job.estimatedCost(job.country);
					job.extendedCost = job.extendedCost(job.country, job.estimatedCost);
					repairjobList.add(job);
					jobCount++;
					break;			
				}//end case1
				
				case 2:{
					if (repairjobList.isEmpty())
						JOptionPane.showMessageDialog(null, "Database empty! Add a Repair Job first...");
						else {
							for(int i = 0; i < repairjobList.size(); ++i)
								repairjobList.get(i).reportData();
						}
						break;
				}//end Case 2
				
				case 3:{
					if (repairjobList.isEmpty())
						JOptionPane.showMessageDialog(null, "Database empty! Add a Repair Job first...");
					else {
						input = JOptionPane.showInputDialog("Enter the JOB ID to search for: ");
						searchJob = input;
						int searchID = Integer.parseInt(searchJob);
						foundAt = searchJobID(searchID);
						if (foundAt == -1)
							// System.out.println(searchSSN + " was not found!");
							JOptionPane.showMessageDialog(null, searchID + " was not found!");
						else
							repairjobList.get(foundAt).reportData();
						break;
					}//end else
					break;
				}//end case 3
				
				case 4:
					JOptionPane.showMessageDialog(null, "Thank you for your business...Goodbye!");
					return;
				
				default:
					JOptionPane.showMessageDialog(null, "Invalid Input, Please select from menu");
					
					
				} //end switch
				
			}//end while(true)
			
		}//end main else
		
		
		
		

	}//end main()
	
	
	public static int Menu() {
		input = JOptionPane.showInputDialog(null, "1.) Create a new Repair Job\n" +
										    "2.) Display all Repair Jobs\n" +
										    	"3.) Search for Repair Job by ID\n" +
										    "4.) Quit the Program"
											, "Vehicle Repair Estimate", JOptionPane.QUESTION_MESSAGE);
		int userInput = Integer.parseInt(input);
		return userInput;
		
	}//end Menu()
	
	
	
	
	public static int searchJobID(int searchID) {
		int i = 0;
		while(i < repairjobList.size()) {
			if (searchID == repairjobList.get(i).jobID)
				return i;
			else
				++i;
		}
		return -1;
	}// end searchJobID

} //end class VehicleRepair Estimate


class RepairJob{
	
	//declaration
	DecimalFormat df = new DecimalFormat("####.##");
	
	
	//object job
	int jobID ;
	String country;
	String serviceCity;
	double estimatedCost;
	double extendedCost;
	
	//empty constructor
	RepairJob(){
		jobID = 0;
		country = "United States";
		serviceCity = "";
		estimatedCost = 0.0;
		extendedCost = 0.0;
		
	}
	
	//constructor with arguments
	RepairJob(int jobID, String country, String serviceCity, double estimatedCost, double extendedCost ){
		this.jobID = jobID;	
		this.country = country;
		this.serviceCity = serviceCity;
		this.estimatedCost = estimatedCost;
		this.extendedCost = extendedCost;
	}
	
	
	int jobID() {
		
		while(true) {
			String input = JOptionPane.showInputDialog(null, "Enter the Job ID: ", "Vehicle Repair Estimate", JOptionPane.QUESTION_MESSAGE);
			int userInput = Integer.parseInt(input);
			if (userInput > 999 || userInput < 100) {
				JOptionPane.showMessageDialog(null, "Invalid Job ID, please enter a valid 3 digit Job ID.");
				continue;
			}//end if
			
			else {
				return userInput;
			}//end else
		}//end while(true) jobID
	}//end jobID()
	
	
	    String country() {
		String selection = "";
		String [] countryList = {"US", "CA"};
		int choice = JOptionPane.showOptionDialog(null, "Select Job Country ", "Vehicle Repair Estimate", 
												JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, 
												countryList, countryList[0]);
		if (choice == 0) {
			return "United States";
		}
		
		else if (choice == 1) {
			return "Canada";
		}
		return "United States";	
	}//end country()
	
	String serviceCity() {
		while (true) {
			String input = JOptionPane.showInputDialog(null,"Enter Job City", "Vehicle Repair Estimate", JOptionPane.QUESTION_MESSAGE );
			boolean isValid = true;
			for (int i = 0; i <input.length(); i++) {
				char c = input.charAt(i);
				if (!Character.isAlphabetic(c) && c != ' ') {
					isValid = false;
					break;
				} // end if-for loop
			}//end if
				
			if (isValid == true) {
				return input;
			}
			
			else {
				JOptionPane.showMessageDialog(null, "City must only contain alphabetic characters or white space only!");
			}	
		}//end while
	}//end serviceCity()
	
	
	double estimatedCost(String jobCountry) {
		
		double cost = 0.0;
		
		String country = jobCountry;
		if (jobCountry.equalsIgnoreCase("United States")) {
			String input = JOptionPane.showInputDialog(null,"Enter Estimate:");
			cost = Double.parseDouble(input);
			return cost;
		}
		else {
			String input = JOptionPane.showInputDialog(null,"Enter Estimate:");
			cost = Double.parseDouble(input);
			double caCost = cost * 1.35;
			return caCost;
		}
		
	}//end estimatedCost()
	
	double extendedCost(String country, double estimatedCost) {
		if (country.equalsIgnoreCase("United States")) {
			return 0.0;
		}
		
		else {
			double cost = estimatedCost + (estimatedCost * 0.10) ;
			return cost;
			
		}//end if-else
	}//end extendedCost()
	
	void reportData() {
		
		if(country.equalsIgnoreCase("Canada")) {
			JOptionPane.showMessageDialog(null, "Job ID: " + jobID + "\n" +
					"Job Country:" + country + "\n" +
					"Job Service City:"  + serviceCity + "\n" +	
					"Job Estimated Cost:$ " + estimatedCost + " CAD\n" +
					"Job Extended Cost:$ " + extendedCost + " CAD\n");
					
		}
		
		else {
			JOptionPane.showMessageDialog(null, "Job ID: " + jobID + "\n" +
					"Job Country:" + country + "\n" +
					"Job Service City:"  + serviceCity + "\n" +	
					"Job Estimated Cost:$ " + estimatedCost + " USD\n" );
					
		}//end if-else
	
	}//end reportData
	
	
	
	
}//end class RepairJob