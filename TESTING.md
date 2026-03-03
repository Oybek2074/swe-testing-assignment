# Testing Strategy – Quick-Calc

## 1. Testing Approach

This project follows a layered testing strategy combining unit tests and integration tests.

Unit tests verify the correctness of individual calculator methods in isolation (add, subtract, multiply, divide, clear). These tests ensure that each function behaves correctly for normal cases and edge cases.

Integration tests verify that different parts of the system work together correctly. In this case, integration tests simulate user-level flows such as performing an operation and then clearing the calculator.

Non-functional aspects such as performance, security, and UI usability were not tested because the project focuses on core logic and functional correctness.

---

## 2. Testing Pyramid

The testing strategy reflects the Testing Pyramid principle:

- Many unit tests (8 tests)
- Fewer integration tests (2 tests)
- No end-to-end UI tests

Most tests are placed at the unit level because unit tests are fast, isolated, and easier to maintain. Integration tests are fewer and focus on verifying overall behavior.

---

## 3. Black-box vs White-box Testing

Unit tests in this project primarily follow white-box testing principles because they directly test known internal methods of the `Calculator` class.

However, integration tests resemble black-box testing since they validate observable behavior (input and output) without focusing on internal implementation details.

---

## 4. Functional vs Non-Functional Testing

This project focuses entirely on functional testing:

- Correct arithmetic results
- Proper exception handling
- Correct reset behavior

Non-functional testing (performance, scalability, security) was intentionally excluded due to the small scope of the application.

---

## 5. Regression Testing

The test suite serves as a regression testing mechanism. Whenever new changes are introduced to the calculator logic, running `pytest` ensures that existing functionality is not broken.

If a future modification introduces an error (for example, incorrect division logic), the existing unit tests will immediately fail, preventing regression.

---

## 6. Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition | Unit | Passed |
| test_subtraction | Unit | Passed |
| test_multiplication | Unit | Passed |
| test_division | Unit | Passed |
| test_division_by_zero | Unit | Passed |
| test_negative_numbers | Unit | Passed |
| test_decimal_numbers | Unit | Passed |
| test_clear_function | Unit | Passed |
| test_full_addition_flow | Integration | Passed |
| test_clear_after_operation | Integration | Passed |