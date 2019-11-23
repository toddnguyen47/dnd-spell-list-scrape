package com.dndSpellList.Controllers;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

import com.dndSpellList.Models.CsvSpellListModel;
import com.dndSpellList.Views.CommandLineInterfaceView;
import com.dndSpellList.utils.CsvReader;

public class CommandLineController {
  private CsvSpellListModel csvSpellListModel = null;
  private CommandLineInterfaceView cliView = null;
  private CsvReader csvReader = null;
  
  private Scanner scanner;
  private String csvFilePath = "";
  private BufferedReader bufReader = null;
  
  private boolean firstLineFlag;
  
  // Getters and setters.
  public String getCsvFilePath() {return this.csvFilePath;}
  public void setCsvFilePath(String csvFilepath) {this.csvFilePath = csvFilepath;}
  public BufferedReader getBufReader() {return this.bufReader;}
  public CsvSpellListModel getCsvSpellListModel() {return this.csvSpellListModel;}
  public CommandLineInterfaceView getCliView() {return this.cliView;}
  
  // Algorithmic functions
  public CommandLineController() {
    this.csvSpellListModel = new CsvSpellListModel();
    this.cliView = new CommandLineInterfaceView();
    this.scanner = new Scanner(System.in);
    
    this.firstLineFlag = true;
  }
  
  /**
   * Main function to run this controller.
   */
  public void invoke() {
    askUserCsvInput();
    readInCsvFile();
  }
  
  public void askUserCsvInput() {
    this.cliView.printCsvInputPrompt();
    this.csvFilePath = this.scanner.nextLine().replace("\\", "/");
    this.cliView.printCsvOutput(this.csvFilePath);
  }
  
  public void readInCsvFile() {
    try {
      this.csvReader = new CsvReader(this.csvFilePath);
      bufReader = this.csvReader.getBufferedReader();
      readCsvLines();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private void readCsvLines() throws IOException {
    while (true) {
      String line = bufReader.readLine();
      if (null == line || line.trim().isEmpty())
        break;
      handleReadLine(line);
    }
  }

  private void handleReadLine(String line) throws IOException {
    if (this.firstLineFlag)
      this.firstLineFlag = false;
    else
      parseLine(line);
  }


  public void parseLine(String curLine) {
    String[] commaSep = curLine.split(",");
    this.csvSpellListModel.addRow(commaSep[0].trim(), commaSep[1].trim());
  }
}
