// Include the required libraries
#include <Arduino.h>

// Define the pin for the load cell signal
const int loadCellPin = 34;  // D34

// Calibration parameters
const float calibrationFactor = 3.33; // Calibration factor obtained from calibration
void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Configure the Serial Plot feature
  Serial.println("#Labels,Weight");
}

void loop() {
  // Read the load cell signal value
  int loadCellValue = analogRead(loadCellPin);
  
  // Convert the load cell value to weight using the calibration factor
  float weight = loadCellValue * calibrationFactor;
  
  // Send the weight data to Serial Plot
  //Serial.print("Force = ");
  Serial.println((weight/100) * 9.8);
  //Serial.println("Newtons");

  delay(500); // Adjust the delay time as needed
}