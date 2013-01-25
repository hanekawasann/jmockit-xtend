package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*

describe "stub behaves like NonStrictExpectations" {
	
	@Mocked
	ExpectationsAPI expectationsAPI
	
	fact "The order and number of call is not important" {
		stub [
			expectationsAPI.returnString
			result = "My string"
			
			expectationsAPI.returnInt
			result = 12345
		]
		
		expectationsAPI.returnString => "My string"
		expectationsAPI.returnString => "My string"
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnString => "My string"
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnSelf => null
	}
	
	fact "Dynamic partial stub" {
		stub(typeof(ExpectationsAPI)) [
			(new ExpectationsAPI).returnString
			result = "My string 1"
		]
		
		(new ExpectationsAPI).returnString => "My string 1" 
		try {
			(new ExpectationsAPI).returnVoid
			fail
		} catch (RuntimeException exception) {
			exception.message => "Not implemented"
		}
		(new ExpectationsAPI).returnString => "My string 1" 
	}
}