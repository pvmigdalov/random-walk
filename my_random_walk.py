import numpy as np
import matplotlib.pyplot as plt

class RandomWalk:
    '''Class for generation random walk'''
    def __init__(self, num_points=5000, start_point=(0, 0)):
        self.num_points = num_points
        self.start_point = start_point

    def get_points(self, r_distribution=(0, 10), phi_distribution=(0, 2 * np.pi)):
        '''
        Generating points using polar coordinates
        r - Uniform[r_distribution]
        phi - Uniform[phi_distribution]
        '''
        r = np.random.uniform(*r_distribution, size=self.num_points - 1)
        phi = np.random.uniform(*phi_distribution, size=self.num_points - 1)

        delta_x = r * np.cos(phi)
        delta_y = r * np.sin(phi)

        x_steps = np.append(np.array([self.start_point[0]]), delta_x)
        y_steps = np.append(np.array([self.start_point[1]]), delta_y)

        self.x = np.cumsum(x_steps)
        self.y = np.cumsum(y_steps)

    def get_distance(self):
        '''The distance between the start and finish'''
        distance = ((self.x[0] - self.x[-1])**2 + (self.y[0] - self.y[-1])**2)**0.5
        return distance

    def plotting(
        self, r_distribution=[0, 10], phi_distribution=[0, 2 * np.pi], 
        cmap='RdPu', point_size=1, alpha=0.5, cbar=True, 
        show_way=False, way_color='black', figsize=(10, 6)
    ):
        '''Vizualization random walk'''
        self.get_points(r_distribution, phi_distribution)
        point_numbers = list(range(self.num_points))
        plt.figure(figsize=figsize)
        plt.title(f'Random walk for {self.num_points} points')
        plt.scatter(self.x, self.y, c=point_numbers, cmap=cmap, s=point_size, alpha=alpha)
        plt.gca().axison = False
        if cbar:
            plt.colorbar()
        plt.scatter(self.x[0], self.y[0], s=1.5*point_size, color='green', label='start')
        plt.scatter(self.x[-1], self.y[-1], s=1.5*point_size, color='red', label='finish')
        if show_way:
            xs = [self.x[0], self.x[-1]]
            ys = [self.y[0], self.y[-1]]
            plt.plot(xs, ys, color=way_color)
            plt.title(f'Random walk for {self.num_points} points; way = {self.get_distance():.2f}')
        plt.legend(loc='best', frameon=False)
        plt.show()
    
    

if __name__ == '__main__':
    rw = RandomWalk(num_points=7999)
    rw.plotting(point_size=1, alpha=0.65, show_way=True, figsize=(7, 4))