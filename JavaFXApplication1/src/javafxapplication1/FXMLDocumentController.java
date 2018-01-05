package javafxapplication1;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.*;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;

/**
 *
 * @author b
 */
public class FXMLDocumentController implements Initializable {
    String checkUsername, checkPassword;
    String uname = "bailey";
    String pword = "bailey";
    
    @FXML private TextField usernameField;
    @FXML private PasswordField passwordField;
    
    @FXML
    private void loginButton(ActionEvent event) {
        checkUsername = usernameField.getText();
        checkPassword = passwordField.getText();
        if (checkUsername.equals(uname) && checkPassword.equals(pword))
        {
            System.out.println("you are logged in.");
        }
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
