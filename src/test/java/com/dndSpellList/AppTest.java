package com.dndSpellList;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class AppTest {
  @Test
  public void testReturnOne() {
    App app = new App();
    Assertions.assertEquals(1, app.returnOne());
    Assertions.assertEquals(2, app.returnOne());
  }
}
