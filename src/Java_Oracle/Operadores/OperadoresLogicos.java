package Java_Oracle.Operadores;

import java.util.Scanner;

public class OperadoresLogicos {
    public static void main(String[] args) {

        //Inicializacion de vectores
        String[] usernames = {"andres", "pablo", "oscar"};
        String[] passwords = {"12124", "32321", "12343"};

        Scanner lectura = new Scanner(System.in);

        System.out.print("Ingrese el nombre usuario: ");
        String u = lectura.next();

        System.out.print("Ingrese el password del usuario: ");
        String p = lectura.next();
        boolean isAuthenticated = false;

        for(int i = 0; i < usernames.length; i++) {
            isAuthenticated = (usernames[i].equals(u) && passwords[i].equals(p));
        }
        String mensaje = isAuthenticated? "Bienvenido usuario ".concat(u).concat("!") : "Lo siento, requiere autenticacion";
        System.out.println(mensaje);

    }
}
