class Calculator
    def initialize(v1, v2)
        @v1 = v1
        @v2 = v2
    end

    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        else
            p 'you tried changing v1 by not integer'
        end
    end

    def add()
        return @v1 + @v2
    end

    def subtract()
        return @v1 - @v2
    end
end

c1 = Calculator.new(10, 10)
p c1.add()
p c1.subtract()

c1.setV1(20)
p c1.add()

c1.setV1('one')
p c1.add()