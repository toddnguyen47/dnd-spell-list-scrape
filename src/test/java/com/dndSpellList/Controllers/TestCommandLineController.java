package com.dndSpellList.Controllers;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.dndSpellList.Models.CsvSpellListModel.Row;

public class TestCommandLineController {
  private CommandLineController clc;
  private String curDir = System.getProperty("user.dir");
  private Path csvFile = Paths.get(
    curDir, 
    "src/test/java/com/dndSpellList/Controllers/testClericSpellList.csv"
  );

  @BeforeEach
  void setUp() {
    clc = new CommandLineController();
    clc.setCsvFilePath(csvFile.toString());
  }
  
  @Test
  @org.junit.jupiter.api.Disabled
  public void testReadingInCsvFile() {
    clc.readInCsvFile();
    assertNotNull(clc.getBufReader());
  }
  
  @Test
  void testReadingIn_IgnoreFirstLine() {
    clc.readInCsvFile();
    assertLine("Guidance,0", 0);
    assertLine("Shield of Faith,1", 21);
    assertLine("Create or Destroy Water,1", 10);
  }
  
  public void assertLine(String curLine, int index) {
    List<Row> l = clc.getCsvSpellListModel().getRows();
    
    String[] expectedList = curLine.split(",");
    assertEquals(expectedList[0].trim(), l.get(index).getSpellName());
    assertEquals(expectedList[1].trim(), l.get(index).getLevel());
  }
}
