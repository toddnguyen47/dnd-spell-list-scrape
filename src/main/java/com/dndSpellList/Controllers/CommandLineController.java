package com.dndSpellList.Controllers;

import java.util.Scanner;

import com.dndSpellList.Models.CsvSpellListModel;
import com.dndSpellList.Views.CommandLineInterfaceView;

public class CommandLineController {
  private CsvSpellListModel csvSpellListModel = null;
  private CommandLineInterfaceView cliView = null;
  private Scanner scanner;
  
  private String csvFilePath = "";
  
  // Getters
  public String getCsvFilePath() {return this.csvFilePath;}
  
  // Algorithmic functions
  public CommandLineController() {
    this.csvSpellListModel = new CsvSpellListModel();
    this.cliView = new CommandLineInterfaceView();
    this.scanner = new Scanner(System.in);
  }
  
  public void invoke() {
    askUserCsvInput();
  }
  
  public void askUserCsvInput() {
    this.cliView.printCsvInputPrompt();
    this.csvFilePath = this.scanner.nextLine().replace("\\", "/");

    this.cliView.printCsvOutput(this.csvFilePath);
  }
}
