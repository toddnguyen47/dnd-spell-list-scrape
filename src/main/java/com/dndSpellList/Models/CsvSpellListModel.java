package com.dndSpellList.Models;

import java.util.ArrayList;
import java.util.List;

public class CsvSpellListModel {
  private class Row {
    private String spellName = "";
    private String level = "";
    
    public Row(String spellName, String level) {
      this.spellName = spellName;
      this.level = level;
    }
    
    public String getSpellName() {return spellName;}
    public String getLevel() {return this.level;}
  }
  
  private List<Row> rows = new ArrayList<>();
  public List<Row> getRows() {return this.rows;}
}
