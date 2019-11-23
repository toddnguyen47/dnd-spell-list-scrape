package com.dndSpellList.utils;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class CsvReader {
  private Path csvFilePath = null;
  
  public CsvReader(String path) {
    this.csvFilePath = Paths.get(path);
  }
  
  public CsvReader(Path path) {
    this.csvFilePath = path;
  }
  
  public BufferedReader getBufferedReader() throws IOException {
    BufferedReader br = Files.newBufferedReader(this.csvFilePath);
    return br;
  }
}
