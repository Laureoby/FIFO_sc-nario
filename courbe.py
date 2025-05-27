import traci
import csv

def run_simulation():
    # Démarre SUMO avec l'interface graphique ou en mode CLI
    traci.start(["sumo-gui", "-c", "fifo.sumocfg"])  # remplace par "sumo-gui" si tu veux voir l’interface graphique

    with open("donnees_simulation.csv", mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["time", "vehicle_id", "speed", "x_position", "y_position"])

        step = 0
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()

            for veh_id in traci.vehicle.getIDList():
                speed = traci.vehicle.getSpeed(veh_id)
                x, y = traci.vehicle.getPosition(veh_id)
                writer.writerow([step, veh_id, speed, x, y])

            step += 1

    traci.close()

if __name__ == "__main__":
    run_simulation()
