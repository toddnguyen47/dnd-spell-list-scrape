package com.dndSpellList.Views;

public class CommandLineInterfaceView {
  public void printCsvInputPrompt() {
    System.out.print("Spell List Filepath: ");
  }
  
  public void printCsvOutput(String csvOutput) {
    System.out.println("String output is: " + csvOutput);
  }
}
