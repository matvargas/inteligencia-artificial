import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class MCell {

    public MCell(int cellX, int cellY){
        this.cellX = cellX;
        this.cellY = cellY;
    }

    public MCell(int cellX, int cellY, char cellType){
        this.cellX = cellX;
        this.cellY = cellY;
        this.cellType = cellType;
    }

    int cellX, cellY;
    char cellType;
}

public class Main {
    public static void main(String [] args) {

        if(args.length < 2){
            System.out.println("Program usage: <Main.java> <[type]algorithm> <entry>");
            return;
        }

        Scanner reader = null;
        try {
             reader = new Scanner(new FileInputStream(args[1]));
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.exit(0);
        }

        int dimX, dimY, W;
        dimX = reader.nextInt();
        dimY = reader.nextInt();
        W = reader.nextInt();

        MCell [][]M = new MCell[dimX][dimY];
        ArrayList<MCell> locPoints = new ArrayList<>();

        int countX = 0;
        while(reader.hasNext()) {
            String fileRow = reader.next();
            for(int i = 0; i < dimY; i++){
                char c = fileRow.charAt(i);
                if(c == '#')
                    locPoints.add(new MCell(countX, i, '#'));
                M[countX][i] = new MCell(countX, i, c);

                System.out.print(M[countX][i] + " ");
            }
            System.out.println(" ");
            countX ++;
        }

        disBtwCells(M[0][0], locPoints.get(0));

        ArrayList<MCell> startPoints = listPossibleStartPoints(M, W, locPoints);

        switch (args[0]){
            case "BFS":
                System.out.println("Finding best path with BFS algorithm");
                break;
            case "DFS":
                System.out.println("Finding best path with DFS algorithm");
                break;
            default:
                break;
        }


    }

    static ArrayList<MCell> listPossibleStartPoints(MCell [][]M, int W, ArrayList<MCell> locPoints) {
        ArrayList<MCell> startPoints = new ArrayList<>();

        return startPoints;
    }

    static int disBtwCells(MCell a, MCell b) {
        int distX = (a.cellX - b.cellX);
        if(distX < 0) distX = distX*(-1);
        int distY = (a.cellY - b.cellY);
        if(distY < 0) distY = distY*(-1);
        return(distX + distY);
    }

}