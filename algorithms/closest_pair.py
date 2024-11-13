import math
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

# Use Agg backend for Matplotlib to save images without displaying
plt.switch_backend('Agg')

def visualize_closest_pair(file_path, output_dir='static/output_images'):
    points = []
    steps = []

     # Empty the output directory if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # Remove all files and subdirectories in output_dir
    os.makedirs(output_dir)  # Recreate the empty directory
    
    # Load points from file
    with open(file_path, 'r') as f:
        for line in f:
            line = line.replace(',', ' ').strip()
            try:
                x, y = map(float, line.split())
                points.append((x, y))
            except ValueError:
                raise ValueError("Invalid input format. Each line should contain two numbers separated by space.")

    # Sort points by x-coordinate for the initial call
    points.sort()
    steps.append(f'Sorted all points by x-coordinate: {points}')

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def dist(p1, p2):
        return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2), 2)

    def save_plot(points, title, step_count, line=None, closest_pair=None, division_line=None):
        plt.figure(figsize=(8, 6))
        plt.scatter(*zip(*points), color="blue")
        if line:
            plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'r--')
        if closest_pair:
            plt.plot([closest_pair[0][0], closest_pair[1][0]], [closest_pair[0][1], closest_pair[1][1]], 'g-', linewidth=2)
            plt.scatter(*zip(*closest_pair), color="green", s=100, edgecolor="black")
        if division_line:
            plt.axvline(x=division_line, color="purple", linestyle="--", linewidth=1.5)
        plt.title(title)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        
        # Save the plot
        filename = f"{output_dir}/step_{step_count}.png"
        plt.savefig(filename)
        plt.close()  # Close plot to free up memory

    def closest_pair_recursive(pts, step_count=0):
        if len(pts) <= 3:
            min_dist = float('inf')
            closest_points = None
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    d = dist(pts[i], pts[j])
                    steps.append(f'Comparing points {pts[i]} and {pts[j]}, distance = {d}')
                    save_plot(pts, f"Comparing {pts[i]} and {pts[j]}", step_count, line=(pts[i], pts[j]))
                    steps.append(f'image step_{step_count}.png')
                    step_count += 1
                    
                    if d < min_dist:
                        min_dist = d
                        closest_points = (pts[i], pts[j])
            steps.append(f'Brute-force result in this segment: {closest_points} with distance {min_dist}')
            return closest_points, min_dist, step_count

        # Divide
        mid = len(pts) // 2
        mid_point = pts[mid]
        steps.append(f'Dividing points at {mid_point} into two halves: {pts[:mid]} and {pts[mid:]}')
        save_plot(pts, f"Dividing at x={mid_point[0]}", step_count, division_line=mid_point[0])
        steps.append(f'image step_{step_count}.png')
        step_count += 1
        

        # Recursive calls on left and right halves
        left_pair, left_min, step_count = closest_pair_recursive(pts[:mid], step_count)
        right_pair, right_min, step_count = closest_pair_recursive(pts[mid:], step_count)
        
        # Conquer
        if left_min < right_min:
            min_dist = left_min
            closest_points = left_pair
        else:
            min_dist = right_min
            closest_points = right_pair
        
        steps.append(f'Closest pair in left side: {left_pair} with distance {left_min}')
        steps.append(f'Closest pair in right side: {right_pair} with distance {right_min}')
        steps.append(f'Minimum distance between halves is {min_dist} from pair {closest_points}')
        save_plot(pts, "Closest pair in left and right", step_count, closest_pair=closest_points)
        steps.append(f'image step_{step_count}.png')
        step_count += 1
        
        
        # Prepare the strip of points close to the middle point
        strip = [pt for pt in pts if abs(pt[0] - mid_point[0]) < min_dist]
        strip.sort(key=lambda p: p[1])  # Sort strip points by y-coordinate
        steps.append(f'Building strip with points close to middle line: {strip}')
        
        # Check minimum distance in the strip
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = dist(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    closest_points = (strip[i], strip[j])
                steps.append(f'Checking strip points {strip[i]} and {strip[j]}, distance = {d}')
                save_plot(strip, f"Checking strip points {strip[i]} and {strip[j]}", step_count, line=(strip[i], strip[j]))
                steps.append(f'image step_{step_count}.png') 
                step_count += 1
                
        
        steps.append(f'After strip check, closest pair is {closest_points} with distance {min_dist}')
        return closest_points, min_dist, step_count

    # Call the recursive function and save the final result
    closest_points, min_distance, step_count = closest_pair_recursive(points)
    result = f'The closest pair is {closest_points} with a distance of {min_distance}'
    save_plot(points, "Final Result", step_count, closest_pair=closest_points)
    steps.append(f'image step_{step_count}.png')
    return steps, result
