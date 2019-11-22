package com.dndSpellList;

import com.dndSpellList.Controllers.CommandLineController;

public class App {
  public static void main(String[] args) {
    App app = new App();
    app.invoke(args);
  }
  
  public App() {}
  
  public void invoke(String[] args) {
    if (cliArgsExists(args))
      handleCliArgs(args);
    else
      handleNoCliArgs();
  }
  
  private boolean cliArgsExists(String[] args) {
    return args.length > 0;
  }
  
  private void handleCliArgs(String[] args) {
    //TODO
    System.out.println("We are in CLI args mode");
    for (String s : args)
      System.out.println(s);
  }
  
  private void handleNoCliArgs() {
    CommandLineController cliController = new CommandLineController();
    cliController.invoke();
  }
}
